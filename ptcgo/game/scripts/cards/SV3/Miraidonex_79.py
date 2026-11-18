from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ec1c7626-b1b7-5c53-811d-2721c0b2a821",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name",
    display_name="Miraidon ex",
    searchable_by=["Miraidon ex", "Basic", "ex", "Miraidonex"],
    subtypes=["Basic", "ex"],
    collector_number=79,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Attack(
            title="Rapid Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Techno Turbo",
            game_text="Attach a Basic Lightning Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            effect=unimplemented,
        ),
    ],
)