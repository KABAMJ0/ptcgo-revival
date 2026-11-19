from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.attacks_common import flip_gate


card = PokemonCardDef(
    guid="69c1437c-2b5d-5ba0-b768-743ce4b1b3b0",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    display_name="Luxio",
    searchable_by=["Luxio", "Stage 1", "Luxio"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    family_id=403,
    abilities=[
        Attack(
            title="Fasten Claws",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(40)),
        ),
        Attack(
            title="Thunder Fang",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)