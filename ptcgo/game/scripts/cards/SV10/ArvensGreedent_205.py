from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="86276f5b-ca74-5c39-8581-4d37b910cbb9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensGreedent.Name",
    display_name="Arven's Greedent",
    searchable_by=["Arven's Greedent", "Stage 1", "ArvensGreedent"],
    subtypes=["Stage 1"],
    collector_number=205,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensSkwovet.Name",
    family_id=819,
    abilities=[
        Ability(
            title="Greedy Order",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put up to 2 Arven's Sandwich cards from your discard pile into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)