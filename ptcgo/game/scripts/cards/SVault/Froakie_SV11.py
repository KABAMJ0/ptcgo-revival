from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import no_energy_free_retreat_passive

card = PokemonCardDef(
    guid="09a170a7-3180-59c1-8efd-c665e32e697d",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    display_name="Froakie",
    searchable_by=["Froakie", "Basic", "Froakie"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=656,
    abilities=[
        Ability(
            title="Frubbles",
            game_text="If this Pok\u00e9mon has any Water Energy attached to it, it has no Retreat Cost.",
            passive=no_energy_free_retreat_passive(inverted=True),
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)