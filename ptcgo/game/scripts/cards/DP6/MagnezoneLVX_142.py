from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import Activations
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.card_effects.passives_common import unafflicted


def _is_lightning_or_metal(card):
    return (energy_provides_type(card, PokemonTypes.LIGHTNING.value)
            or energy_provides_type(card, PokemonTypes.METAL.value))


def _electric_trans_condition(board, player_id, pokemon):
    return unafflicted(board, player_id, pokemon)         and can_move_energy(_is_lightning_or_metal)(board, player_id, pokemon)


async def _cyber_shock(ctx):
    await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=lambda card: energy_provides_type(
            card, PokemonTypes.LIGHTNING.value),
        prompt="Discard a Lightning Energy attached to Magnezone")
    await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=lambda card: energy_provides_type(
            card, PokemonTypes.METAL.value),
        prompt="Discard a Metal Energy attached to Magnezone")
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="6d5fe875-7551-5ef8-b917-18078ccd2969",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneLVX.Name",
    display_name="Magnezone LV.X",
    searchable_by=["Magnezone LV.X", "Level-Up", "MagnezoneLVX"],
    subtypes=["Level-Up"],
    collector_number=142,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    family_id=462,
    abilities=[
        Ability(
            title="Electric Trans",
            condition=_electric_trans_condition,
            activation=Activations.UNLIMITED,
            game_text="As often as you like during your turn (before your attack), you may move a Lightning or Metal Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Magnezone is affected by a Special Condition.",
            effect=move_energy_between(predicate=_is_lightning_or_metal, count=1),
        ),
        Attack(
            title="Cyber Shock",
            game_text="Discard a Lightning Energy and a Metal Energy attached to Magnezone. The Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1},
            damage=80,
            effect=_cyber_shock,
        ),
    ],
)