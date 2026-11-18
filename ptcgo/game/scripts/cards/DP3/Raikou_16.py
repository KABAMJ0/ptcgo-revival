from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="36f7a679-8bab-5487-9630-52365899a143",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=243,
    abilities=[
        Ability(
            title="Thunder Rumble",
            game_text="Once during your turn (before your attack), when you attach a Lightning Energy card from your hand to Raikou, you may put 1 damage counter on 1 of your opponent's Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Thunder Climb",
            game_text="Discard 3 cards from the top of your deck. This attack does 50 damage plus 10 more damage for each Lightning Energy card you discarded. Then, attach those Lightning Energy cards to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)