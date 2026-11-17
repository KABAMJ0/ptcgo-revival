from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="acd4baf9-d201-562c-8ca6-56c710ba0e1e",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HydreigonEX.Name",
    display_name="Hydreigon-EX",
    searchable_by=["Hydreigon-EX", "Basic", "EX", "HydreigonEX"],
    subtypes=["Basic", "EX"],
    collector_number=62,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=635,
    abilities=[
        Ability(
            title="Dragon Road",
            game_text="If there is any Stadium card in play, the Retreat Cost of each of your Dragon Pok\u00e9mon in play is ColorlessColorless less.",
            effect=unimplemented,
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)