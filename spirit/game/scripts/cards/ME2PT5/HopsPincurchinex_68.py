from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="db9e7c68-a26b-5562-b331-817f5a21205e",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsPincurchinex.Name",
    display_name="Hop's Pincurchin ex",
    searchable_by=["Hop's Pincurchin ex", "Basic", "ex", "HopsPincurchinex"],
    subtypes=["Basic", "ex"],
    collector_number=68,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=871,
    abilities=[
        Ability(
            title="Counterattack Quills",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), place 3 damage counters on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Spiky Thunder",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)