from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4453467d-7e8f-5f80-b1f7-8fff85aaaf88",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StaraptorFB.Name",
    display_name="Staraptor FB",
    searchable_by=["Staraptor FB", "Basic", "SP", "StaraptorFB"],
    subtypes=["Basic", "SP"],
    collector_number=11,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=398,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(20)),
        ),
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)