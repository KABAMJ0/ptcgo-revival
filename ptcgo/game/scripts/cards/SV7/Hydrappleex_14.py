from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4aac6eeb-6e65-5cfe-a1a1-d779f10c79e5",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydrappleex.Name",
    display_name="Hydrapple ex",
    searchable_by=["Hydrapple ex", "Stage 2", "ex", "Hydrappleex"],
    subtypes=["Stage 2", "ex"],
    collector_number=14,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Ripening Charge",
            game_text="Once during your turn, you may attach a Basic Grass Energy card from your hand to 1 of your Pok\u00e9mon. If you attached Energy to a Pok\u00e9mon in this way, heal 30 damage from that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Syrup Storm",
            game_text="This attack does 30 more damage for each Grass Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)