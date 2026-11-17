from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="52c00b0e-7c65-533e-b315-aeb74d673c53",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasManectric.Name",
    display_name="Team Aqua's Manectric",
    searchable_by=["Team Aqua's Manectric", "Stage 1", "TeamAquasManectric"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasElectrike.Name",
    family_id=309,
    abilities=[
        Ability(
            title="Power Shift",
            game_text="Once during your turn (before your attack), you may move any number of basic Energy cards attached to 1 of your Pok\u00e9mon with Team Aqua in its name to another of your Pok\u00e9mon. This power can't be used if Team Aqua's Manectric is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Thunderspark",
            game_text="Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's) that has Energy cards attached to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)