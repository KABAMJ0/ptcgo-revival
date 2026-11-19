from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5460df38-dd19-535b-b374-faa3df375bad",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaMeganiumex.Name",
    display_name="Mega Meganium ex",
    searchable_by=["Mega Meganium ex", "Stage 2", "MEGA", "ex", "MegaMeganiumex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=10,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=360,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Attack(
            title="Giant Bouquet",
            game_text="This attack does 50 more damage for each Grass Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=damage_per(count_energy("self", "grass"), 50),
        ),
    ],
)