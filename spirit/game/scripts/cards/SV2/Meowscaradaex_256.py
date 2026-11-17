from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4532f141-a619-5c28-996c-e699dd825ee2",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowscaradaex.Name",
    display_name="Meowscarada ex",
    searchable_by=["Meowscarada ex", "Stage 2", "ex", "Meowscaradaex"],
    subtypes=["Stage 2", "ex"],
    collector_number=256,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    family_id=906,
    abilities=[
        Ability(
            title="Bouquet Magic",
            game_text="You must discard a Basic Grass Energy card from your hand in order to use this Ability. Once during your turn, you may put 3 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Scratching Nails",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)