from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b8fed851-546a-5873-845a-4e76943c60cc",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minior.Name",
    display_name="Minior",
    searchable_by=["Minior", "Basic", "Minior"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=774,
    abilities=[
        Ability(
            title="Far-Flying Meteor",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, when you attach an Energy card from your hand to this Pok\u00e9mon, you may switch it with your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Gravitational Tackle",
            game_text="This attack does 20 damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)