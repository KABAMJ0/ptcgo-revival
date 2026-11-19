from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import def_for
def _is_react(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() == "react energy"


def _react_count(pokemon) -> int:
    return sum(1 for energy in (getattr(pokemon, "children", None) or [])
               if _is_react(energy))


def _attacker_has_react(ctx) -> bool:
    return ctx.attacker is not None and _react_count(ctx.attacker) > 0


async def _devolution_wave(ctx):
    """Devolve up to one opponent Evolved Pokemon per React Energy on Cradily;
    the removed evolution cards are shuffled into the opponent's deck."""
    limit = _react_count(ctx.attacker)
    evolved = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
               if pokemon.get_attribute(AttrID.STAGE) in (
                   PokemonStage.STAGE1.value, PokemonStage.STAGE2.value)]
    if limit <= 0 or not evolved:
        return
    picked = await ctx.choose_cards(
        evolved, min(limit, len(evolved)), minimum=0,
        prompt="Choose Evolved Pokémon to devolve")
    for pokemon in picked:
        removed = await ctx.devolve_pokemon(pokemon, 1, destination="hand")
        if removed:
            await ctx.shuffle_into_deck(removed, ctx.opponent_id)


card = PokemonCardDef(
    guid="7efab587-876e-55dd-8758-88dd5fe348c9",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name",
    display_name="Cradily",
    searchable_by=["Cradily", "Stage 2", "Cradily"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    family_id=345,
    abilities=[
        Attack(
            title="Devolution Wave",
            game_text="Count the number of React Energy cards attached to Cradily and choose up to that number of your opponent's Evolved Pok\u00e9mon. Remove the highest Stage Evolution card from each of those Pok\u00e9mon, then have your opponent shuffle those cards into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_devolution_wave,
        ),
        Attack(
            title="Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(30, pool="any"),
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)