from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eaf0e46d-9919-5938-82a8-8d876efa4afd",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume δ",
    searchable_by=["Vileplume \u03b4", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=45,
    abilities=[
        Ability(
            title="Poison Pollen",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Poisoned. This power can't be used if Vileplume is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Poltergeist",
            game_text="Look at your opponent's hand. This attack does 30 damage plus 10 more damage for each Trainer card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)