from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a00c203e-f358-5457-beed-438ae508e8cd",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    display_name="Roselia",
    searchable_by=["Roselia", "Basic", "Roselia"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="DP1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=315,
    abilities=[
        Attack(
            title="Toxic Spikes",
            game_text="The Defending Pok\u00e9mon is now Poisoned. If Roselia is evolved from Budew, this attack does 10 damage to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Sweet Spike",
            game_text="The Defending Pok\u00e9mon is now Asleep. Remove 2 damage counters from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=10,
            effect=unimplemented,
        ),
    ],
)