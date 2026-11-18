from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e1859868-24eb-56d5-9742-454d6bb5b384",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2", "Vivillon"],
    subtypes=["Stage 2"],
    collector_number=193,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Attack(
            title="Evo-Powder",
            game_text="For each of your Benched Pok\u00e9mon, search your deck for a card that evolves from that Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.GRASS: 1},
            damage=90,
        ),
    ],
)