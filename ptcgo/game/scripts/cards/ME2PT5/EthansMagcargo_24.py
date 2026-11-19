from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import no_energy_free_retreat_passive


card = PokemonCardDef(
    guid="99c2f848-4a82-508b-ad0b-948da94469e3",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansMagcargo.Name",
    display_name="Ethan's Magcargo",
    searchable_by=["Ethan's Magcargo", "Stage 1", "EthansMagcargo"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSlugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Melt Away",
            game_text="If this Pok\u00e9mon has no Energy attached, it has no Retreat Cost.",
            passive=no_energy_free_retreat_passive(),
        ),
        Attack(
            title="Lava Burst",
            game_text="Discard up to 5 Fire Energy from this Pok\u00e9mon. This attack does 70 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 3},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)