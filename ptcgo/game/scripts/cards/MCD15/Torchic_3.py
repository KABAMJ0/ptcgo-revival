from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="30c3b85b-0ffb-5525-966d-e4d9be061bba",
    key="MCD15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    display_name="Torchic",
    searchable_by=["Torchic", "Basic", "Torchic"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="MCD15",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=255,
    abilities=[
        Attack(
            title="Ember",
            game_text="Flip a coin. If tails, discard a Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)