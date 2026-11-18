from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b2fcdf7b-b15f-591b-a0ec-2a51f0300a83",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Samurott.Name",
    display_name="Samurott",
    searchable_by=["Samurott", "Stage 2", "Samurott"],
    subtypes=["Stage 2"],
    collector_number=107,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    family_id=501,
    abilities=[
        Ability(
            title="Torrential Whirlpool",
            game_text="Once during your turn, you may switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.)",
            effect=unimplemented,
        ),
        Attack(
            title="Energized Slash",
            game_text="This attack does 50 more damage for each Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)