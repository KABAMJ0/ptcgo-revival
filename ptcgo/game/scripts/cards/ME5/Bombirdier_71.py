from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="06bc420b-c411-53cf-ac97-2fa37986456c",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdier.Name",
    display_name="Bombirdier",
    searchable_by=["Bombirdier", "Basic", "Bombirdier"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=962,
    abilities=[
        Attack(
            title="Challenging Delivery",
            game_text="Flip 2 coins. If both of them are heads, search your deck for a Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Speed Wing",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)