from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.pokemon import in_active_spot


async def scorching_feathers(ctx):
    """If this Pokémon (in the Active Spot) is damaged by an attack, burn the attacker."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    await ctx.apply_special_condition(ctx.damaged_by, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="fdf19ba1-ee46-57ef-bbe2-650d504b2755",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    display_name="Numel",
    searchable_by=["Numel", "Basic", "Numel"],
    subtypes=["Basic"],
    collector_number=223,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=322,
    abilities=[
        Ability(
            title="Incandescent Body",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Burned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=scorching_feathers,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)