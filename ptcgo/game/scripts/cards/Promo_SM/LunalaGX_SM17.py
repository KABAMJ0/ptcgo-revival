from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f463a52e-51ec-5fb8-ab4c-a89e923cc6ed",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LunalaGX.Name",
    display_name="Lunala-GX",
    searchable_by=["Lunala-GX", "Stage 2", "GX", "LunalaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=17,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=792,
    abilities=[
        Ability(
            title="Psychic Transfer",
            game_text="As often as you like during your turn (before your attack), you may move a Psychic Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Moongeist Beam",
            game_text="The Defending Pok\u00e9mon can't be healed during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=120,
            effect=unimplemented,
        ),
        Attack(
            title="Lunar Fall-GX",
            game_text="Knock Out 1 of your opponent's Basic Pok\u00e9mon that isn't a Pok\u00e9mon-GX. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=unimplemented,
        ),
    ],
)