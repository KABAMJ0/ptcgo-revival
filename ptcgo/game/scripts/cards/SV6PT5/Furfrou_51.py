from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="f37d7733-55b9-5564-84fe-0e09f454a61d",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name",
    display_name="Furfrou",
    searchable_by=["Furfrou", "Basic", "Furfrou"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SV6PT5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=676,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Attach a Basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=attach_from_discard(is_basic_energy_card, count=1, target="choice"),
        ),
    ],
)