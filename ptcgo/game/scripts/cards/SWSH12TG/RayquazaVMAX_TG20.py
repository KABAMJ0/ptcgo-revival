from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ec5a6dc1-3dc0-5f08-9095-7b3e12a62633",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaVMAX.Name",
    display_name="Rayquaza VMAX",
    searchable_by=["Rayquaza VMAX", "VMAX", "Rapid Strike", "RayquazaVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=20,
    set_code="SWSH12TG",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaV.Name",
    family_id=384,
    abilities=[
        Ability(
            title="Azure Pulse",
            game_text="Once during your turn, you may discard your hand and draw 3 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Max Burst",
            game_text="You may discard any amount of basic Fire Energy or any amount of basic Lightning Energy from this Pok\u00e9mon. This attack does 80 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)