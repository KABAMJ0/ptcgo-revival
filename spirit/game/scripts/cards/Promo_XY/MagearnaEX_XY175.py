from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7bafe9c7-eb6c-5b9a-a750-993feaa785f7",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagearnaEX.Name",
    display_name="Magearna-EX",
    searchable_by=["Magearna-EX", "Basic", "EX", "MagearnaEX"],
    subtypes=["Basic", "EX"],
    collector_number=175,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=801,
    abilities=[
        Ability(
            title="Mystic Heart",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to each of your Pok\u00e9mon that has any Metal Energy attached to it. (Existing effects are not removed.)",
            effect=unimplemented,
        ),
        Attack(
            title="Soul Blaster",
            game_text="During your next turn, this Pok\u00e9mon's Soul Blaster attack's base damage is 60.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)