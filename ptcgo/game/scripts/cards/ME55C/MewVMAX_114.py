from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7e4325fe-22d5-5564-a29f-3b69efce1801",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewVMAX.Name",
    display_name="Mew VMAX",
    searchable_by=["Mew VMAX", "VMAX", "MewVMAX"],
    subtypes=["VMAX"],
    collector_number=114,
    set_code="ME55C",
    rarity=Rarities.RareHolo,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MewV.Name",
    family_id=151,
    abilities=[
        Attack(
            title="Cross Fusion Strike",
            game_text="Choose 1 of your Benched Fusion Strike Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Max Miracle",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)