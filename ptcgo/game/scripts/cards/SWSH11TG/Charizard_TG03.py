from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ba844d8-f7d2-5aef-b985-18b254438c19",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SWSH11TG",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=6,
    abilities=[
        Ability(
            title="Battle Sense",
            game_text="Once during your turn, you may look at the top 3 cards of your deck and put 1 of them into your hand. Discard the other cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Royal Blaze",
            game_text="This attack does 50 more damage for each Leon card in your discard pile.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)