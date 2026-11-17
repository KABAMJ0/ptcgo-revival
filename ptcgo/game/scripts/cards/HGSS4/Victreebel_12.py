from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d64610a-daf7-5eaf-9929-d1cc6632f732",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2", "Victreebel"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="HGSS4",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Ability(
            title="Tangling Tendrils",
            game_text="As long as Victreebel is your Active Pok\u00e9mon, your opponent's Active Pok\u00e9mon's Retreat Cost is ColorlessColorless more.",
            effect=unimplemented,
        ),
        Attack(
            title="Acidic Drain",
            game_text="The Defending Pok\u00e9mon is now Burned and Poisoned. Remove 3 damage counters from Victreebel.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)