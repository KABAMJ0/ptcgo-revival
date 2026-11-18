from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="562f5db6-779b-50b5-9889-4e76bdd86717",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic", "Growlithe"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Vaporize",
            game_text="Discard a Water Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)