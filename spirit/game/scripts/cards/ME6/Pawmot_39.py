from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="75670e6b-c957-55c5-acb9-e384d4605718",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmot.Name",
    display_name="Pawmot",
    searchable_by=["Pawmot", "Stage 2", "Pawmot"],
    subtypes=["Stage 2"],
    collector_number=39,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    family_id=921,
    abilities=[
        Ability(
            title="Generator's Touch",
            game_text="Once during your turn, you may use this Ability. Attach a Basic Lightning Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Electric Punch",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)