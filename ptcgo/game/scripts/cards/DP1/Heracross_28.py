from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="98ea3032-1d9e-57fa-84ca-d8aa041d8efa",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic", "Heracross"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Pitch",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Horn Slash",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(60)),
        ),
    ],
)