from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7d8b5130-dbd4-51ae-9cec-23e39511ca07",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=374,
    abilities=[
        Attack(
            title="Core Beam",
            game_text="Discard a Metal Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)