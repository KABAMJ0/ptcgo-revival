from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f378fa8f-e83c-5376-bd2e-cef83761947c",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kommoo.Name",
    display_name="Kommo-o",
    searchable_by=["Kommo-o", "Stage 2", "Kommoo"],
    subtypes=["Stage 2"],
    collector_number=75,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    family_id=782,
    abilities=[
        Ability(
            title="Beat Scales",
            game_text="Once during your turn, you may use this Ability. Look at the top 6 cards of your deck and attach any number of Basic Energy cards you find there to your Dragon Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=170,
        ),
    ],
)