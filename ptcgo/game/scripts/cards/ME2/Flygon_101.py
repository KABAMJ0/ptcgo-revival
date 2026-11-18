from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb7c8647-707d-5cf1-b00f-25122d655476",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=101,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Sandy Flapping",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may use this Ability. You may also use this Ability if this Pok\u00e9mon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon. Discard the top 2 cards of your opponent's deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.FIGHTING: 2},
            damage=130,
        ),
    ],
)