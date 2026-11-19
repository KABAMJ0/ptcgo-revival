from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import in_active_spot


async def commotion(ctx):
    """Active Spot only: damaged by an opponent's attack (even if Knocked
    Out) and 2 damage counters go on each of your Benched Pokemon."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    for pokemon in ctx.my_bench():
        await ctx.deal_damage(20, target=pokemon, apply_modifiers=False,
                              as_counters=True)
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack


card = PokemonCardDef(
    guid="5614ad3d-1e7e-5573-a7e0-079ff8785fe4",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="DM",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Ability(
            title="Commotion",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 2 damage counters on each of your Benched Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=commotion,
        ),
        Attack(
            title="Wild Tail",
            game_text="You may discard any Stadium card in play.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=discard_stadium_attack(optional=True),
        ),
    ],
)