from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="f166b66e-5304-5058-9a07-0638ac7dd19b",
    key="FUT20",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScorbunnyontheBall.Name",
    display_name="Scorbunny on the Ball",
    searchable_by=["Scorbunny on the Ball", "Basic", "ScorbunnyontheBall"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="FUT20",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=813,
    abilities=[
        Attack(
            title="Fiery Dribbling",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(per_heads=20, until_tails=True),
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)