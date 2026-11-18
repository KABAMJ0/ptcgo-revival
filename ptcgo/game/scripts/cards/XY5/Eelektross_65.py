from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6d39d43a-79ab-5b26-bdbb-7fca309e8ec8",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name",
    display_name="Eelektross",
    searchable_by=["Eelektross", "Stage 2", "Eelektross"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Ability(
            title="Energy Connect",
            game_text="As often as you like during your turn (before your attack), you may move a basic Energy attached to 1 of your Benched Pok\u00e9mon to your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Electricannon",
            game_text="You may discard all Lightning Energy attached to this Pok\u00e9mon. If you do, this attack does 50 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)