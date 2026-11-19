from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for


async def _supreme_blast(ctx):
    """Supreme Blast: nothing without both LV.X partners in play."""
    names = {_display_name(p) for p in ctx.my_pokemon_in_play()}
    if not {"Uxie LV.X", "Azelf LV.X"} <= names:
        return
    await ctx.deal_damage()
    if ctx.attacker is not None:
        energies = list(ctx.attached_energies(ctx.attacker))
        if energies:
            await ctx.discard_cards(energies)


def _display_name(entity) -> str:
    """The printed name of a card on the board (empty when unknown)."""
    return getattr(def_for(getattr(entity, "archetype_id", "") or ""),
                   "display_name", "") or ""

card = PokemonCardDef(
    guid="26eedc2b-7976-56d3-98b5-3359c8913236",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MespritLVX.Name",
    display_name="Mesprit LV.X",
    searchable_by=["Mesprit LV.X", "Level-Up", "MespritLVX"],
    subtypes=["Level-Up"],
    collector_number=143,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name",
    family_id=481,
    abilities=[
        Attack(
            title="Healing Look",
            game_text="Remove 3 damage counters from each of your Benched Pok\u00e9mon.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Supreme Blast",
            game_text="If don't have Uxie LV.X and Azelf LV.X in play, this attack does nothing. Discard all Energy attached to Mesprit.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=200,
            effect=_supreme_blast,
        ),
    ],
)