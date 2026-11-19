from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.card_effects.attacks_common import flip_gate


async def _vine_bind(ctx):
    ctx.lock_poke_powers()


async def _vine_bind(ctx):
    ctx.lock_poke_powers()


card = PokemonCardDef(
    guid="5e2e25b9-bbd5-54e5-b275-f6a5b2192c2d",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    display_name="Bellsprout",
    searchable_by=["Bellsprout", "Basic", "Bellsprout"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Attack(
            title="Vine Bind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't use any Pok\u00e9-Powers during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_gate(then=_vine_bind),
        ),
        Attack(
            title="Careless Tackle",
            game_text="Bellsprout does 10 damage to itself.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=recoil_attack(10),
        ),
    ],
)