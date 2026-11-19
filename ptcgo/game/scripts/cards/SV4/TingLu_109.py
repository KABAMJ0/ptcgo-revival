from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, is_basic_energy_card

card = PokemonCardDef(
    guid="55d31782-0ebd-5758-b873-27e797b1ec4c",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TingLu.Name",
    display_name="Ting-Lu",
    searchable_by=["Ting-Lu", "Basic", "TingLu"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=1003,
    abilities=[
        Attack(
            title="Sand Bringer",
            game_text="Attach up to 2 Basic Fighting Energy cards from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=attach_from_discard(basic_energy_of("fighting"), count=2, minimum=0, target="choice"),
        ),
        Attack(
            title="Arrogant Impact",
            game_text="If this Pok\u00e9mon has 4 or more damage counters on it, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=220,
            effect=unimplemented,
        ),
    ],
)