from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3c31c80a-7218-5b14-afe9-df18ec63c089",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TogekissEX.Name",
    display_name="Togekiss-EX",
    searchable_by=["Togekiss-EX", "Basic", "EX", "TogekissEX"],
    subtypes=["Basic", "EX"],
    collector_number=83,
    set_code="XY9",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=468,
    abilities=[
        Attack(
            title="Mighty Wind",
            game_text="You may attach an Energy card from your hand to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Hurricane Wing",
            game_text="Flip 4 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=50),
        ),
    ],
)