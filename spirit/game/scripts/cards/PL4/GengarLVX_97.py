from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df928864-8c64-544a-af1d-90d76b9e28c6",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GengarLVX.Name",
    display_name="Gengar LV.X",
    searchable_by=["Gengar LV.X", "Level-Up", "GengarLVX"],
    subtypes=["Level-Up"],
    collector_number=97,
    set_code="PL4",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Level-Down",
            game_text="Once during your turn (before your attack), you may choose 1 of your opponent's Pok\u00e9mon LV.X. Remove the Level-Up card from that Pok\u00e9mon and have your opponent shuffle that card into his or her deck. The power can't be used if Gengar is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Compound Pain",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon that already has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)