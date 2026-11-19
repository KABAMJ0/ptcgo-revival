from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.data_utils import def_for
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


def _latias_in_play(pokemon, board) -> bool:
    """'If you have Latias or Latias ex in play' on the holder's own side."""
    for other in board.pokemon_in_play(pokemon.owning_player_id):
        definition = def_for(getattr(other, "archetype_id", "") or "")
        name = (getattr(definition, "display_name", "") or "").lower()
        if name.startswith("latias") and "-" not in name:
            return True
    return False


class _DeltaAuraPsychicForce(Passive):
    """With Latias in play, Latios's Psychic Force costs Lightning Metal
    Colorless (printed: Lightning Metal Colorless Colorless Colorless)."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        if (cost.get("Colorless") != 3 or cost.get("Lightning") != 1
                or cost.get("Metal") != 1):
            return cost
        if not _latias_in_play(pokemon, board):
            return cost
        cost["Colorless"] = 1
        return cost


async def _psychic_force(ctx):
    """Nothing at all unless the opponent has a Stage 2 Evolved Pokemon."""
    if any(pokemon.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value
           for pokemon in ctx.opponent_pokemon_in_play()):
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="e699d246-7f47-5b1d-98d6-dc3890e83e16",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios δ",
    searchable_by=["Latios \u03b4", "Basic", "Latios"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    family_id=381,
    abilities=[
        Ability(
            title="Delta Aura",
            game_text="If you have Latias or Latias ex in play, the attack cost of Latios's Psychic Force is now Lightning MetalColorless.",
            passive=_DeltaAuraPsychicForce(),
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Psychic Force",
            game_text="If your opponent has no Stage 2 Evolved Pok\u00e9mon in play, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=_psychic_force,
        ),
    ],
)