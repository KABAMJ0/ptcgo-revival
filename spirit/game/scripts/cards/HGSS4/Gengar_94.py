from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b45c0e9f-312e-5288-91d1-e8558b2f8063",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Prime", "Gengar"],
    subtypes=["Stage 2", "Prime"],
    collector_number=94,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Catastrophe",
            game_text="As long as Gengar is your Active Pok\u00e9mon, if any of your opponent's Pok\u00e9mon would be Knocked Out, put that Pok\u00e9mon in the Lost Zone instead of discarding. (Discard all cards attached to that Pok\u00e9mon.)",
            effect=unimplemented,
        ),
        Attack(
            title="Hurl into Darkness",
            game_text="Look at your opponent's hand and choose a number of Pok\u00e9mon you find there up to the number of Psychic Energy attached to Gengar. Put the Pok\u00e9mon you chose in the Lost Zone.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Cursed Drop",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)