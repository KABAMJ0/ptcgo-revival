from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_defender_attacks


async def freezing_chill(ctx):
    await ctx.deal_damage()
    lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="cfc4505b-aed7-5f78-a433-9ac52157e049",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Appletun.Name",
    display_name="Appletun",
    searchable_by=["Appletun", "Stage 1", "Appletun"],
    subtypes=["Stage 1"],
    collector_number=140,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Melting Sweetness",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=freezing_chill,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=130,
            effect=recoil_attack(20),
        ),
    ],
)