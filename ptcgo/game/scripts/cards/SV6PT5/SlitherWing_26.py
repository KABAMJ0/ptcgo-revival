from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="22577a35-cc76-5a90-b4cb-f167b501ee10",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SlitherWing.Name",
    display_name="Slither Wing",
    searchable_by=["Slither Wing", "Basic", "Ancient", "SlitherWing"],
    subtypes=["Basic", "Ancient"],
    collector_number=26,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Iron Smasher",
            game_text="If your opponent has any Future Pok\u00e9mon in play, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Smashing Wing",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)