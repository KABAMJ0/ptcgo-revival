from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5000e30b-414e-545f-8e48-82314e5d2a9d",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="BASE1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Thunder",
            game_text="Flip a coin. If tails, Zapdos does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy cards attached to Zapdos in order to use this attack.",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)