from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce397bca-fa8f-58d5-8667-d30937f8affa",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftryex.Name",
    display_name="Shiftry ex",
    searchable_by=["Shiftry ex", "Stage 2", "ex", "Shiftryex"],
    subtypes=["Stage 2", "ex"],
    collector_number=97,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Skill Hack",
            game_text="Look at your opponent's hand and choose a Basic Pok\u00e9mon or Evolution card you find there. Choose 1 of that Pok\u00e9mon's attacks. Skill Hack copies that attack except for its Energy cost. (You must still do anything else required for that attack.) (No matter what type that Pok\u00e9mon is, Shiftry ex's type is still Darkness.) Shiftry ex performs that attack.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dirge",
            game_text="Does 60 damage to each of your opponent's Benched Pok\u00e9mon that has the same name as the Defending Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)