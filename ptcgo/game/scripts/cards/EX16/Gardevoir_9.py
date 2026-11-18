from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="72e1da19-30d9-5654-9bb1-a446e704d2d0",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Psy Shadow",
            game_text="Once during your turn (before your attack), you may search your deck for a Psychic Energy card and attach it to 1 of your Pok\u00e9mon. Put 2 damage counters on that Pok\u00e9mon. Shuffle your deck afterward. This power can't be used if Gardevoir is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Burst",
            game_text="Does 10 damage times the total amount of Energy attached to Gardevoir and the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)