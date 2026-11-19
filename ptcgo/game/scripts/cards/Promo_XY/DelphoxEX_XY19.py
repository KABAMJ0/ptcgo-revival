from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="cd1814d1-80df-579c-bdb8-ec6a06e6649a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DelphoxEX.Name",
    display_name="Delphox-EX",
    searchable_by=["Delphox-EX", "Basic", "EX", "DelphoxEX"],
    subtypes=["Basic", "EX"],
    collector_number=19,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=655,
    abilities=[
        Attack(
            title="Psybeam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Wonder Flare",
            game_text="Your opponent reveals his or her hand. This attack does 40 more damage for each Energy card in your opponent's hand.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)