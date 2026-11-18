from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a3e9afd1-d0be-53a3-b231-d337eb4781fa",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic", "Prime", "Absol"],
    subtypes=["Basic", "Prime"],
    collector_number=91,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=359,
    abilities=[
        Ability(
            title="Eye of Disaster",
            game_text="As long as Absol is your Active Pok\u00e9mon, whenever your opponent puts a Basic Pok\u00e9mon from his or her hand onto his or her Bench, put 2 damage counters on that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Vicious Claw",
            game_text="Choose 1 Pok\u00e9mon from your hand and put it in the Lost Zone. (If you can't put a Pok\u00e9mon in the Lost Zone, this attack does nothing.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)