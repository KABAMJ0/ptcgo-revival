from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="18482cb5-3963-55a2-bc80-308a537de733",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwoex.Name",
    display_name="Mewtwo ex",
    searchable_by=["Mewtwo ex", "Basic", "Tera", "ex", "Mewtwoex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=58,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[
        Attack(
            title="Transfer Charge",
            game_text="Attach up to 2 Basic Psychic Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Photon Kinesis",
            game_text="This attack does 30 more damage for each Psychic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)